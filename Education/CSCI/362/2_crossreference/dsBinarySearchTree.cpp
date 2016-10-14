
#include <string>
#include <iostream>     // std::cout
#include <stdlib.h>     /* atoi */
using namespace std;
#include "dsBinarySearchTree.h" 


//////////////////////////////////////////////////////////////////////////// 
// constructor
//////////////////////////////////////////////////////////////////////////// 
dsBinarySearchTree::dsBinarySearchTree(){
    treeRoot = NULL; // set root to NULL
}


void dsBinarySearchTree::outputTable(){
    outputThisNode(treeRoot);
    cout << endl << "-------------" << endl;
}

void dsBinarySearchTree::outputThisNode(treeNode* thisNode){
    if(thisNode == NULL){
        return;   
    }

    // First output left elements
    outputThisNode(thisNode->left);

    // then output self
    std::string keyword = thisNode->word;
    while(keyword.length() < 10){
        keyword += " ";   
    }
    cout << keyword << " | "; 

    listNode* thisListNode = thisNode->listRoot;
    while(thisListNode != NULL){
        cout << " " << thisListNode->val << " ";
        thisListNode = thisListNode->next;
    }
    cout << endl;

    // then output right elements
    outputThisNode(thisNode->right);

}


void dsBinarySearchTree::addWordToTree(std::string theWord, int lineNumber){
    //cout << "Adding to tree word " << theWord << endl; 
    treeNode* newNode = createNewNode(theWord, lineNumber);  

    if(treeRoot == NULL){
        //cout << "Creating Root" << endl;   
        treeRoot = newNode;
        //cout << treeRoot->word << endl;
        return;
    } 

    addNewNodeToTreeRecursivly(newNode, treeRoot, 0);

    /*
    cout << treeRoot->word << endl;
    if(treeRoot->left != NULL){
        cout << "left - " << treeRoot->left->word << endl;
    } else {
        cout << "left - null" << endl;   
    }
    if(treeRoot->right != NULL){
        cout << "right - " << treeRoot->right->word << endl;
    } else {
        cout << "right - null" << endl;   
    }
    */

    //outputTable();

}

void dsBinarySearchTree::addThisLineNumberToThisList(listNode* newListNode, listNode* listRoot){
    listNode* thisNode = listRoot;
    while(thisNode->next != NULL){
        thisNode = thisNode->next;   
    }
    thisNode->next = newListNode;
}

void dsBinarySearchTree::addNewNodeToTreeRecursivly(treeNode* newNode, treeNode* thisRoot, int wordCharIndex){
    if(thisRoot == NULL){
        cout << "ROOT IS NULL - ERROR!" << endl; 
        return;
    }

    if(newNode->word == thisRoot->word){
        //cout << "SAME WORD!"<< endl;
        // Add lineNumber to thisRoot
        listNode* newListNode = newNode->listRoot;
        listNode* listRoot = thisRoot->listRoot;
        addThisLineNumberToThisList(newListNode, listRoot);
        return;
    }

    //cout << ", " << thisRoot->word << ", ";
    char theWordChar = newNode->word[wordCharIndex];
    char balanceChar = thisRoot->word[wordCharIndex];

    if(theWordChar == balanceChar){ // If the characters are equal
        wordCharIndex++;
        return addNewNodeToTreeRecursivly(newNode, thisRoot, wordCharIndex); // run the function again with incremented wordCharIndex   
    } 
    else     
    if (theWordChar < balanceChar){ 
        // add left of thisRoot
        //cout << "left";
        if(thisRoot->left == NULL){
            thisRoot->left = newNode; 
            //cout << " Done " << endl;
        } else {
            addNewNodeToTreeRecursivly(newNode, thisRoot->left, 0);
        }
    } 
    else
    if (theWordChar > balanceChar){
        // add right of thisRoot
        //cout << "right";
        if(thisRoot->right == NULL){
            thisRoot->right = newNode; 
            //cout << " Done " << endl;
        } else {
            addNewNodeToTreeRecursivly(newNode, thisRoot->right, 0);
        }
    }
}

dsBinarySearchTree::treeNode* dsBinarySearchTree::createNewNode(std::string theWord, int lineNumber){
    listNode* newListNode = new listNode(); // create new listNode
    newListNode->val = lineNumber;

    treeNode* newNode = new treeNode();   // create new treeNode
    newNode->listRoot = newListNode;
    newNode->word = theWord;
}
    
