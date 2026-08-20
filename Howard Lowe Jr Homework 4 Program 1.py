


class OrderNode:
    
# this class node would store the customer's order
    def __init__(self, order_id, name, fooditem):

        self.order_id = order_id
        self.name = name
        self.fooditem = fooditem

        
        self.next = None


class OrderQueue:
    

    def __init__(self):
        # front points to the first order waiting to be processed
        self.front = None

        # rear points to the most recently inserted order
        self.rear = None

    def is_empty(self):
        
        return self.front is None  # this will happen when queue contains no orders

    def insert_order(self, order_id, name, fooditem):
        

        # this function would display all items from lowest price to the
        #  highest price
        new_order = OrderNode(order_id, name,fooditem )

        # So if the query, the  order  will become
        #  both the front and then the rear.
        if self.is_empty():
            self.front = new_order
            self.rear = new_order

        else:
            # connecting the current rear node to the new order.
            self.rear.next = new_order

            # moving rear to the new last order.
            self.rear = new_order

        print("\nOrder was added successfully.")

    def delete_order(self):
        

        if self.is_empty():
            print("\nThe order queue is empty.")
            print("There are no orders to process.")
            return

        # saving the front order before removing it.
        completed_order = self.front

        # this will move the  front to the next order.
        self.front = self.front.next

        # if front becomes None, the queue is empty.
        # rear must also become None.
        if self.front is None:
            self.rear = None

        print(" The completed order below: ")
        

        print("Order ID: ", completed_order.order_id)
        print("Customer: ", completed_order.name)

        print("Food Item:", completed_order.fooditem)
        

    def display_orders(self):
       # whats occuring is the O(n) as every order in this queue must be visited

        if self.is_empty():
            print("The order queue is empty.")

            return

        current = self.front # The time complexity being done is O(1) as its checking whether front is None or not. 

        print("Current Online Orders")
        


        position = 1

        while current is not None:
            print("Queue's Position:", position)
            print("Order ID:", current.order_id)
            print("Customer's Name:", current.name)
            print("Food Item:", current.fooditem)
            

            current = current.next
            position += 1

        print("Front order is processed first.")
      


def queuemenu():
    

# these are the options to do the operations from queue
    print("The Food Delivery Onlne Queue")
    print("1. Insert a new order")
    print("2. Process or delete an order")
    print("3. Display all the orders")
    print("4. Exit")


def main():
    orderqueue = OrderQueue()

    while True:
        queuemenu()

        choice = input("Please choose one of the options: ")

        if choice == "1": # asking you for a new order
            order_id = input(" Thank you. Please, enter the order ID: ")

            name = input("Thank you. Please, enter the customer's name: ")

            fooditem = input("Thank you. Please, enter the food item: ")

            orderqueue.insert_order(order_id, name, fooditem)

        elif choice == "2":
# using delte_order function
            orderqueue.delete_order()

        elif choice == "3":

            orderqueue.display_orders()
# using display_orders function
        elif choice == "4":

            print("Thanks for using the ordering system!!")

        

        else:

            print("Option selected is an invalid selection. Please enter one of displayed options.")



if __name__ == "__main__":
    main()