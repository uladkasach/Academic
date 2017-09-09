#include <string>
#include <iostream>     // std::cout
using namespace std;
#include "dsLinkedList.h"

    
//////////////////////////////////////////////////////////////////////////// 
// constructor
//////////////////////////////////////////////////////////////////////////// 
dsLinkedList::dsLinkedList(){
    root = NULL; // set root to NULL
    head = NULL; // set head to NULL
}
//////////////////////////////////////////////////////////////////////////// 
//////////////////////////////////////////////////////////////////////////// 

//////////////////////////////////////////////////////////////////////////// 
// Define Method make sure head is at last node of list. Self Explanitory.
//////////////////////////////////////////////////////////////////////////// 
void dsLinkedList::makeSureHeadIsAtLastNodeOfList(){
    while(head->next != NULL){
        head = head->next;   
    }
}
//////////////////////////////////////////////////////////////////////////// 
//////////////////////////////////////////////////////////////////////////// 
    
//////////////////////////////////////////////////////////////////////////// 
// Define Method for Adding a Node to end of list
//////////////////////////////////////////////////////////////////////////// 
void dsLinkedList::addNode(int iPos, int jPos){
    //////////////////////////////////////
    // Define New Node
    //////////////////////////////////////
    Node *newNode = new Node();   // create new Node
    //cout << "new node : " << newNode << endl;

    newNode->iPos = iPos;             // set values
    newNode->jPos = jPos;

    newNode->next = NULL;         // make next equal to null, since it is going to be last in list.
    newNode->prev = head;         // make it point to the node before it. - Sets to null if its the first node. 

    if(head != NULL){
        //cout << "Head is at " << head->iPos << "," << head->jPos << endl;
    }
    
    //////////////////////////////////////
    // Link last node in list to new node
    //////////////////////////////////////
    if(head != NULL){
        makeSureHeadIsAtLastNodeOfList();
        head->next = newNode;
    }

    //////////////////////////////////////
    // If this is the first node, make root point to it.
    //////////////////////////////////////
    if(head == NULL){ 
        root = newNode;
    }

    head = newNode;               // last but not least, make the head point at the new node.
    //cout << "here : " << head << endl;
    //cout << "here : " << root << endl;
}
//////////////////////////////////////////////////////////////////////////// 
//////////////////////////////////////////////////////////////////////////// 

//////////////////////////////////////////////////////////////////////////// 
// Read off the values of every element in the list
//////////////////////////////////////////////////////////////////////////// 
void dsLinkedList::readAll(){
    //cout << "Reading Initial Conditions Stored" << endl;
    int index = 1;
    Node *nextNode = root; // Just give it a value other than null so that we can use Null to stop the reading loop. It also serves as a starting node. Worked out well.
    Node *thisNode;
    while(nextNode != NULL){
        thisNode = nextNode;
        //cout << thisNode << endl;
        cout << "#" << index << " (" << thisNode->iPos << "," << thisNode->jPos << ")" << endl;
        nextNode = thisNode->next;
        index += 1;
    }
    if(index == 1){
        cout << "EMPTY" << endl;   
    }
}

int dsLinkedList::length(){
    // count the total number of nodes and return int   
    int index = 0;
    Node *nextNode = root;
    Node *thisNode;
    while(nextNode != NULL){
        index += 1;
        thisNode = nextNode;
        nextNode = thisNode->next;
    }
    return index;
}

dsLinkedList::Node* dsLinkedList::selectNodeAtIndex(int selectIndex){
    int index = 0;
    Node *thisNode = root;
    while(index < selectIndex){
        thisNode = thisNode->next;
        index += 1;
    }
    return thisNode;
}

void dsLinkedList::removeNode(int removalIndex){
    //cout << "removing node at index " << removalIndex << endl;   
    
    Node *thisNode = selectNodeAtIndex(removalIndex);
    
    if(thisNode == NULL){
        return;   
    }
    
    if(thisNode->prev != NULL){
        thisNode->prev->next = thisNode->next;   
    }
    
    if(thisNode->next != NULL){
        thisNode->next->prev = thisNode->prev;   
    }
    
    head = thisNode->prev;
    
    delete thisNode;
    
}

void dsLinkedList::modifyNode(int modifyIndex, int iPos, int jPos){
    Node *thisNode = selectNodeAtIndex(modifyIndex);
    thisNode->iPos = iPos;
    thisNode->jPos = jPos;
    cout << iPos << jPos << endl;
}


int* dsLinkedList::getPositionFor(int index){
    Node* thisNode = selectNodeAtIndex(index);
    
    int* position = new int[2];
    position[0] = thisNode->iPos;
    position[1] = thisNode->jPos;
    
    return position;   
}


//////////////////////////////////////////////////
//////////////////////////////////////////////////
    
