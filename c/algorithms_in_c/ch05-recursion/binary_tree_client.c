#include <stdio.h>
#include <stdlib.h>

#include "binary_tree.h"
#include "stack.h"

#define TREE_MAX 20

// this tree comes from figure 5-26;
link create_tree()
{
    link root = new_node('E');
    link d = new_node('D');
    link h = new_node('H');
    root->left = d;
    root->right = h;

    link b = new_node('B');
    b->left = new_node('A');
    b->right = new_node('C');
    d->left = b;

    link f = new_node('F');
    f->right = new_node('G');
    h->left = f;

    return root;
}

void visit_node(link node)
{
    printf("%c ", node->item);
}

void pre_order(link tree, void (*visit)(link))
{
    if(tree == NULL)
        return;

    visit(tree);
    pre_order(tree->left, visit);
    pre_order(tree->right, visit);
}


void pre_order_non_recur(link tree, void (*visit)(link))
{
    stack_init(TREE_MAX);
    stack_push(tree);

    while (!stack_isempty())
    {
        visit(tree = stack_pop());
        if (tree->right != NULL)
        {
            stack_push(tree->right);
        }
        if (tree->left != NULL)
        {
            stack_push(tree->left);
        }
    }
}

void in_order(link tree, void (*visit)(link))
{
    if(tree == NULL)
        return;

    in_order(tree->left, visit);
    visit(tree);
    in_order(tree->right, visit);
}

void post_order(link tree, void (*visit)(link))
{
    if(tree == NULL)
        return;

    post_order(tree->left, visit);
    post_order(tree->right, visit);
    visit(tree);
}

int main(int argc, char *argv[])
{
    link tree = create_tree();

    printf("preorder: \n");
    pre_order(tree, visit_node);

    printf("\n");
    printf("inorder: \n");
    in_order(tree, visit_node);

    printf("\n");
    printf("postorder: \n");
    post_order(tree, visit_node);

    printf("\n");
    printf("pre_order_non_recur: \n");
    pre_order_non_recur(tree, visit_node);

    printf("\n");
    printf("tree count: %d \n", tree_count(tree));

    return 0;
}
