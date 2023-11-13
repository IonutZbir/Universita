#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linked_list.h"

// create a new object that contains an integer
object new_int(int val){
    object obj = {'u', NULL};
    obj.type = INT;
    obj.val = malloc(sizeof(int));
    *(int *)obj.val = val;
    return obj;
}

// create a new object that contains a float
object new_float(float val){
    object obj;
    obj.type = FLOAT;
    obj.val = malloc(sizeof(float));
    *(float *)obj.val = val;
    return obj;
}

// create a new object that contains a long
object new_long(long val){
    object obj;
    obj.type = LONG;
    obj.val = malloc(sizeof(long));
    *(long *)obj.val = val;
    return obj;
}

// create a new object that contains a doubke
object new_double(double val){
    object obj;
    obj.type = DOUBLE;
    obj.val = malloc(sizeof(double));
    *(double *)obj.val = val;
    return obj;
}

// create a new object that contains a char
object new_char(char val){
    object obj;
    obj.type = CHAR;
    obj.val = malloc(sizeof(char));
    *((char *)obj.val) = val;
    return obj;
}

// create a new object that contains a string
object new_string(char *val){
    object obj;
    obj.type = STRING;
    obj.val = malloc(sizeof(char) * (strlen(val) + 1));
    obj.val = strcpy(obj.val, val);
    return obj;
}

// initialize a NULL list
linked_list ll_init(void)
{
    linked_list l = {NULL, 0};
    return l;
}

// insert a node in position 0 with int data
linked_list ll_in0_int(linked_list list, int value)
{
    object obj = new_int(value);
    node *nd = malloc(sizeof(node));
    nd->data.type = obj.type;
    nd->data.val = obj.val;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// insert a node in position 0 with float data
linked_list ll_in0_float(linked_list list, float value)
{
    object obj = new_float(value);
    node *nd = malloc(sizeof(node));
    nd->data = obj;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// insert a node in position 0 with long data
linked_list ll_in0_long(linked_list list, long value)
{
    object obj = new_long(value);
    node *nd = malloc(sizeof(node));
    nd->data = obj;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// insert a node in position 0 with double data
linked_list ll_in0_double(linked_list list, double value)
{
    object obj = new_double(value);
    node *nd = malloc(sizeof(node));
    nd->data = obj;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// insert a node in position 0 with char data
linked_list ll_in0_char(linked_list list, char value)
{
    object obj = new_char(value);
    node *nd = malloc(sizeof(node));
    nd->data = obj;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// insert a node in posizion 0 with string data
linked_list ll_in0_string(linked_list list, char *value)
{
    object obj = new_string(value);
    node *nd = malloc(sizeof(node));
    nd->data = obj;
    nd->next = list.head;
    list.head = nd;
    list.len++;
    return list;
}

// delete the node in position 0
linked_list ll_del0(linked_list list)
{
    node *nd = list.head;
    list.head = nd->next;
    free(nd);
    list.len--;
    return list;
}

/*
    it searchs the node in position "pos" of the list
    if the node does not exist it returns NULL
    it the node exists, returns a pointer to the node
*/ 
node *ll_search(linked_list list, int pos)
{
    // TODO: binary search
    node *nd = list.head;
    int i = 0;
    while (nd != NULL && i < pos)
    {
        nd = nd->next;
        i++;
    }
    return nd;
}

// inserts a node with int data in the position "pos" 
linked_list ll_insert_int(linked_list list, int pos, int value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_int(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data.type = obj.type;
        nd->data.val = obj.val;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_int(list, value);
    }
    return list;
}

// inserts a node with float data in the position "pos" 
linked_list ll_insert_float(linked_list list, int pos, float value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_float(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data = obj;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_float(list, value);
    }
    return list;
}

// inserts a node with long data in the position "pos" 
linked_list ll_insert_long(linked_list list, int pos, long value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_long(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data = obj;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_long(list, value);
    }
    return list;
}

// inserts a node with double data in the position "pos" 
linked_list ll_insert_double(linked_list list, int pos, double value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_double(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data = obj;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_double(list, value);
    }
    return list;
}

// inserts a node with char data in the position "pos" 
linked_list ll_insert_char(linked_list list, int pos, char value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_char(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data = obj;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_char(list, value);
    }
    return list;
}

// inserts a node with string data in the position "pos" 
linked_list ll_insert_string(linked_list list, int pos, char *value)
{
    node *pre_node, *nd;
    if (pos > 0 && pos <= list.len)
    {
        object obj = new_string(value);
        pre_node = ll_search(list, pos - 1);
        /*
            pointer to the node in the position before the node to be inserted
        */
        nd = malloc(sizeof(node)); // the node to be inserted
        nd->data = obj;
        nd->next = pre_node->next;
        pre_node->next = nd;
        list.len++;
    }
    else if (pos == 0)
    {
        list = ll_in0_string(list, value);
    }
    return list;
}

linked_list ll_delete(linked_list list, int pos)
{
    node *pre_node, *pos_node;
    if (pos > 0 && pos < list.len)
    {
        pre_node = ll_search(list, pos - 1);
        pos_node = pre_node->next;
        pre_node->next = pos_node->next;
        free(pos_node);
        list.len--;
    }
    else if (pos == 0 && list.len > 0)
    {
        list = ll_del0(list);
    }

    return list;
}

// prints the list in the format: ( a, b, c, d, ... )
void ll_print(linked_list list)
{
    node *nd = list.head;
    char nd_type;
    int index = 0;
    printf("( ");
    while (nd != NULL)
    {
        nd_type = nd->data.type;
        switch (nd_type)
        {
        case INT:
            printf("%d", (*(int *)nd->data.val));
            break;
        case FLOAT:
            printf("%f", (*(float *)nd->data.val));
            break;
        case LONG:
            printf("%ld", (*(long *)nd->data.val));
            break;
        case DOUBLE:
            printf("%lf", (*(double *)nd->data.val));
            break;
        case CHAR:
            printf("%c", (*(char *)nd->data.val));
            break;
        case STRING:
            printf("%s", nd->data.val);
            break;
        default:
            break;
        }
        if (index < list.len - 1) {
            printf(", ");
        }
        nd = nd->next;
        index++;
    }
    printf(" )\n");
}
