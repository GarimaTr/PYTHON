marks= {
    "Jay":89,
    "Shankar":56,
    "kira":"light",
    98:"Jay"
}
print(marks,type(marks))
print(marks["kira"])
print(marks.items(),type(marks.items()))
print(marks.values())
marks.update({"Jay":67,"Renuka":89})
print(marks)
print(marks.get("Jay"))
print(marks["Jay"])
print(marks["Jay2"])   #retuns an error
print(marks.get("Jay3"))  #prints none 


