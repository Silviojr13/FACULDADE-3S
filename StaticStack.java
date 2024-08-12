public class StaticStack {
    private int[] stack;
    private int top;
    private int maxSize;
    
    public StaticStack(int size) {
        maxSize = size;
        stack = new int[maxSize];
        top = -1;
    }

    public void push(int value) {
        if (isFull()) {
            System.out.println("Pilha está cheia. Não é possível adicionar o elemento: " + value);
        } else {
            stack[++top] = value;
            System.out.println("Elemento " + value + " adicionado à pilha.");
        }
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Pilha está vazia. Não é possível remover elementos.");
            return -1; 
        } else {
            int value = stack[top--];
            System.out.println("Elemento " + value + " removido da pilha.");
            return value;
        }
    }

    public void clear() {
        top = -1;
        System.out.println("Pilha foi limpa.");
    }

    public boolean isFull() {
        return top == maxSize - 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }


    public void printStack() {
        if (isEmpty()) {
            System.out.println("Pilha está vazia.");
        } else {
            System.out.print("Elementos na pilha: ");
            for (int i = 0; i <= top; i++) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        StaticStack stack = new StaticStack(5);

        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);

        stack.printStack();

        stack.pop();
        stack.printStack();

        stack.clear();
        stack.printStack();
    }
}
