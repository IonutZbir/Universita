typedef enum Types{
    INT = 'i',
    FLOAT = 'f',
    CHAR = 'c',
    STRING = 's',
    LONG = 'l',
    DOUBLE = 'd'
}Types;

typedef struct keys{
    char **array;
    int len;    
}keys;

typedef struct values{
    float *array;
    int len;    
}values;

typedef struct object{
    Types type; // type of the value
    void *val; // pointer to the value
}object;

typedef struct node{
    char *key;
    object data;
    struct node *next;
}node;

typedef struct dict{
    node **head;
    int len;
    int cap;
}dict;

dict dict_init(int);
dict dict_resize(dict, int);
dict dict_set_int(dict, char*, int);
dict dict_set_float(dict, char*, float);
dict dict_set_long(dict, char*, long);
dict dict_set_double(dict, char*, double);
dict dict_set_char(dict, char*, char);
dict dict_set_string(dict, char*, char*);
node* dict_search(dict, char*);
node* dict_in0(node*, node);
char** get_keys(dict);
float* get_values(dict);
int dict_del(dict, char*);
int hash(dict, char*);
void llist_print(node*);
void dict_print(dict);
void llist_print_debug(node*);
void dict_print_debug(dict);