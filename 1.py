class node:
    def __init__(self,cdll,data,prev_node,next_node):
        self.next=next_node
        self.data=data
        self.prev=prev_node
        if cdll.isempty() :
            self.next=self
            self.prev=self
        else:
            (self.prev).next=self
            (self.next).prev=self
class cdll:
    def __init__(self):
        self.lsita=[]
    def isempty(self):
        print("[is empty]",not len(self.lsita))
        return not len(self.lsita)
    def join(self,node):
        self.lsita.append(node)
    def get_node(self,data,data_next):
        for i in self.lsita:
            if(i.data == data and i.next.data == data_next):

                return i
    def print_node(self):
        for i in self.lsita:
            print(i.prev.data,"<---------",i.data,"-------->",i.next.data)
    def delete_node(self,node):
        if self.isempty():
            return
        elif len(self.lsita) == 1:
            (self.lsita).remove(node)
        else:
            temp=node.next
            temp.prev=node.prev
            (node.prev).next=temp
            (self.lsita).remove(node)
model=cdll()
model.join(node(model,0,None,None))
model.join(node(model,1,model.get_node(0,0),model.get_node(0,0)))
model.join(node(model,5,model.get_node(0,1),model.get_node(1,0)))
model.print_node()
model.delete_node(model.get_node(0,5))
model.print_node()
