
class ClassUserManager {
    protected static $WalletManager; // ClassWalletManager Object
    protected static $Hashbrown = null; // HashbrownClass Object -- Used To hash password one-way so that passwords are not stored on server
    protected static $mysqliAccess = null;
    protected $userData = null;
    
    /////////////////////////////////////
    // Setter Functions: Set Static Variables
    /////////////////////////////////////
    function setWalletManager($WalletManager){      ## Set WalletManager object
        self::$WalletManager = $WalletManager; 
    }
    function setMySqli($var){                       ## Set mysqliAccess object 
        if(!($var instanceof MySQLi)){
            print "Variable Passed to set mysqli is not a mysqli object. Error.";
            die();
        }
        self::$mysqliAccess = $var;
        return true;
    }
    function setHashbrown($var){                    ## Set Hashbrown object
        self::$Hashbrown = $var;
    }
    
    /////////////////////////////////////
    // Getter Functions : Get Data
    /////////////////////////////////////
    function returnUserData(){                      ## Get user data
        $data = self::$userData;
        return $data; 
    }
    function isSignedIn(){                          ## Check if user is signed in
        if(null !== $userData){
            return true;   
        } else {
            return false;   
        }
    }
    
    /////////////////////////////////////
    // Find User
    ////////////////////////////////////
    function lookupUserBy($key, $value){            ## Find a user by a key value pair from database
        $valid_keys = [
            "username" => [
                    "query" => "SELECT UserID FROM Users WHERE Username = ?",
                ],
            /*
            example of how else one might look up a user in the future
            "lookupKey" => [
                    "query" => "SELECT UserID FROM Users WHERE LookupKey = ?",     
                ],
            */
            ];
        
        $thisQuery = $valid_keys[$key]["query"];
        if(!isset($thisQuery)){
            print "That Lookup Key ($key) is not defined. Error.";
            die();
        }
        
        $mysqli = self::$mysqliAccess;
        $stmt = $mysqli->prepare($thisQuery);
        //print "SELECT Title, FilePath, DateTimeAdded, Views, Downloads FROM Schedules WHERE LocationID = '".$locationID."' AND Alive = '1'";
        print   $mysqli->error ;
        $stmt->bind_param("s", $value);
        $stmt->execute();
        $stmt->store_result();
        $numRows = $stmt->num_rows;
        //print $num_of_rows;
        $stmt->bind_result($userID);  
        while ($stmt->fetch()) {}
        $stmt->free_result();
        $stmt->close();

        if($numRows == 0){
            return false;   
        }
        return $userID;
    }
    
    
    /////////////////////////////////////
    // Return data for user by ID
    /////////////////////////////////////
    function returnHashDataForID($userID){
        $mysqli = self::$mysqliAccess;
        $stmt = $mysqli->prepare("SELECT Hash FROM Users WHERE UserID = ?");
        //print "SELECT Title, FilePath, DateTimeAdded, Views, Downloads FROM Schedules WHERE LocationID = '".$locationID."' AND Alive = '1'";
        print   $mysqli->error;
        $stmt->bind_param("s", $userID);
        $stmt->execute();
        $stmt->store_result();
        $numRows = $stmt->num_rows;
        //print $num_of_rows;
        $stmt->bind_result($hash);  
        while ($stmt->fetch()) {
            $hash = $hash;
        }
        $stmt->free_result();
        $stmt->close();

        if($numRows == 0){
            return false;   
        }
        return $hash;
    }
    function returnUserDataForID($userID){
        $mysqli = self::$mysqliAccess;
        $stmt = $mysqli->prepare("SELECT WalletID FROM Users WHERE UserID = ?");
        //print "SELECT Title, FilePath, DateTimeAdded, Views, Downloads FROM Schedules WHERE LocationID = '".$locationID."' AND Alive = '1'";
        print   $mysqli->error ;
        $stmt->bind_param("s", $userID);
        $stmt->execute();
        $stmt->store_result();
        $numRows = $stmt->num_rows;
        //print $num_of_rows;
        $stmt->bind_result($walletID);  
        while ($stmt->fetch()) {
            $userData = [
                    "id" => $userID,
                    "walletID" => $walletID,
                ];
        }
        $stmt->free_result();
        $stmt->close();

        if($numRows == 0){
            return false;   
        }
        return $userData;
    }
    
    /////////////////////////////////////
    // LOGOUT
    /////////////////////////////////////
    function logUserOut(){                          ## Log User Out
        self::$userData = null;
    }
    
    /////////////////////////////////////
    // REGISTER
    /////////////////////////////////////
    function attemptUserRegistration($username, $password){
        ## Verify that the username is unique
        $userID = self::lookupUserBy("username", $email);
        if($userID == false) {
            return 'ALREADY_REGISTERED';
        }
        ## Register the user, since the username is unique
        $userID = registerUser($username, $password);
        ## Sign the user in, now that they are registered
        attemptUserLogin($username, $password);
    }
    function registerUser($username, $password){    ## Register a user with given username and password
        //print "Beginning Registration";
        $username = strtolower($username);
        $hash = self::$Hashbrown->create_hash($password);
        
        /////////////////////////
        // Insert User into Users
        ////////////////////////
        $mysqli = self::$mysqliAccess;
        $when = date('Y-m-d H:i:s');
        $stmt = $mysqli->prepare("INSERT INTO Users (`DateTimeAdded`, `Username`, `Hash`) VALUES (?, ?, ?)");
        //print "INSERT INTO Users (`DateTimeAdded`, `Email`) VALUES ('$when', '$email')";
        echo $mysqli->error;
        $stmt->bind_param("sss", $when, $username, $hash);
        $exec = $stmt->execute();
        $stmt->close();
        ////////////////////////
        var_dump($exec);
        $userID = $mysqli->insert_id;
        //print "here i am!";
        var_dump($userID);
        
        /////////////////
        // Return User ID
        /////////////////
        return $userID;
    }
    
    
    /////////////////////////////////////
    // LOGIN
    /////////////////////////////////////
    function attemptUserLogin($username, $password){
        /////////////////////////
        // Find the user with the given username
        /////////////////////////
        $userID = self::lookupUserBy("username", $username);
        $hash = self::returnHashDataForID($userID);
        //var_dump($hash);
        
        /////////////////////////
        // Security Measure: 
        // If the username is not registered, make a fake password 
        //   and still run the validation function in order to keep
        //   the time spent validating registered usernames and unregistered
        //   usernames equal. This eliminates the possibility of learning 
        //   which usernames are registered and which are not based on validation time.
        /////////////////////////
        if($hash == false){
            $hash = "sha256:1000:abcdefg:1234567";
        }

        /////////////////////////
        // Make sure the passwords match
        /////////////////////////
        $result = self::$Hashbrown->validate_password($password, $hash);
        if($result !== true){
            return false;   
        }
        
        /////////////////////////
        // Log the user in
        /////////////////////////
        $result = self::logUserIn($userID);
        return $result;
    }
    function generateUserDataForID($userID){
        $data = returnUserDataForID($userID);
        $walletID = $data['walletID'];
        $userData = [
                "id" => $userID,
                "walletID" => $walletID,
            ];
        return $userData;
    }
    protected function logUserIn($userID){
        $userData = self::generateUserDataForID($userID);
        self::$userData = $userData; 
        return true;
    }
};