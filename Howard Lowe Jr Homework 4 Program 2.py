


class productnode:
    

    def __init__(self, productid, productname, price):
        self.productid = productid
        self.productname = productname
        self.price = price

       # These are the nodes
        self.left = None
        self.right = None


class productcatalog:
    

    def __init__(self):
        self.root = None

    def insert_product(self, productid, productname, price):
        
        # whats occuring here is the time complexity of O(log n )
        # this involves in the the while True loop,
        #  algorithm would go down the tree

        new_product = productnode(productid, productname, price)

        # so when the tree is empty, the new product becomes the root.
        if self.root is None:
            self.root = new_product
            print("\nProduct added successfully.")
            return

        current = self.root

        while True:

            # So lower price is being inserted into the left tree.
            if price < current.price:

                if current.left is None:
                    current.left = new_product
                    break

                current = current.left

            # An equal or higher price is inserted into
            # the right subtree.
            else:

                if current.right is None:
                    current.right = new_product
                    break

                current = current.right

        print("\nProduct added successfully.")

    def ordertraversal(self):
        

        if self.root is None:
            print("\nThe product catalog is empty.")
            return

        
        stack = []

        # Start at the root of the tree.
        current = self.root

        print("\nProducts Sorted by Price")
        

        productnumber = 1

        # The while loop will continue
        #  while there is a current node or
        # while the stack still contains nodes.
        while current is not None or len(stack) > 0:

            
            while current is not None:
                stack.append(current)       
                current = current.left

            # This removes the most recently inserted node.
            current = stack.pop()           

            # displaying the node.
            print("Product Number :", productnumber)
            print("Product ID :", current.productid)
            print("Product Name :", current.productname)
            print(f"Price: ${current.price:,.2f}")
            

            productnumber += 1

            # after visiting the node, this will examine its right subtree.
            current = current.right

        


def display_catalog_menu():
   

    print("\nOnline Product Catalog")
    print("1. Insert a product")
    print("2. Display products in ascending price order")
    print("3. Exit the catalog")


def main():
    catalog = productcatalog()

    while True:
        display_catalog_menu()

        choice = input("Enter your selection: ")

        if choice == "1":

            productid = input("Please, enter the product ID: ")
            productname = input("Please, enter the product name: ")

            try:

                price = float(input("Next, please enter the product price: $"))


                if price < 0:

                    print("The price cannot be negative! ")

                    print("only positive please.")
                    continue # this only done to prevent error

            except ValueError:

                print("The price is invalid! Please enter a number.")


                continue # only used to prevent error


            catalog.insert_product(productid, productname, price)

        elif choice == "2":

            catalog.ordertraversal()


        elif choice == "3":


            print("\nThank you for using the product catalog!")

            break

        else:
            print("Option selection is invalid. Please enter options 1, 2, or 3. Thank you.")



if __name__ == "__main__":
    main()