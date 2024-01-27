class TreeNode:
    def __init__(self,data, children = []):
        self.data = data
        self.children = children

    def __str__(self,level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)


drinks = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
hot = TreeNode("Hot",[])

cola = TreeNode("Cola",[])
fanta = TreeNode("Fanta",[])
pepsi = TreeNode("Pepsi",[])

cold.addChild(cola)
cold.addChild(fanta)
cold.addChild(pepsi)

tea = TreeNode("Tea",[])
coffee = TreeNode("Coffee",[])

hot.addChild(tea)
hot.addChild(coffee)

drinks.addChild(cold)
drinks.addChild(hot)

print(drinks)
