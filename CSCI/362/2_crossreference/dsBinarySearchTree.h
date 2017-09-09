#ifndef dsBinarySearchTree_EXISTS
#define dsBinarySearchTree_EXISTS     
// dont forget #endif at bottom

class dsBinarySearchTree {
    //////////////////////////////////////////////////
    protected:
    //////////////////////////////////////////////////
        struct listNode {
            int val;
            listNode* next;
        };
        struct treeNode {
            std::string word;
            listNode *listRoot;
            treeNode *left;
            treeNode *right;
        };
        treeNode *treeRoot;  
    //////////////////////////////////////////////////
    //////////////////////////////////////////////////


    //////////////////////////////////////////////////
    public:
    //////////////////////////////////////////////////
        //////////////////////////////////////////////////////////////////////////// 
        // constructor
        //////////////////////////////////////////////////////////////////////////// 
        dsBinarySearchTree();
        //////////////////////////////////////////////////////////////////////////// 
        //////////////////////////////////////////////////////////////////////////// 

        void outputTable();
    
        void outputThisNode(treeNode* thisNode);
    
        void addWordToTree(std::string theWord, int lineNumber);
    
        void addThisLineNumberToThisList(listNode* newListNode, listNode* listRoot);
    
        void addNewNodeToTreeRecursivly(treeNode* newNode, treeNode* thisRoot, int wordCharIndex);
    
        treeNode* createNewNode(std::string theWord, int lineNumber);
    
};



#endif 