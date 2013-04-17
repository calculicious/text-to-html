class Person:
    number = 0
    fname = ""
    lname = ""
    def __init__(self,number,fname,lname):
        self.number= number
        self.fname = fname
        self.lname = lname
        
    def __lt__ (self, other):
        if self.lname == other.lname:
            return self.fname < other.fname
        return self.lname < other.lname

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.fname == other.fname and self.lname == other.lname

    def __ne__ (self, other):
        return not self.__eq__(other)


f = open("input.txt")

#load all data into text
text = f.read()
f.close()

#remove line breaks
temp = ""
for line in text.splitlines():
    temp = temp + " " + line

text = temp

#create a list of all tokens
text_list= text.split()
person_list = []
index = 0
while(index < len(text_list)):
    if text_list[index].isdigit():
        person_list.append(Person(int(text_list[index]),text_list[index+1],text_list[index+2]))
        index = index + 2
    index = index + 1

#now all of the data is in people_list

#sort people
person_list.sort()

#build output html
html_text = '<html><style>table{border-collapse:collapse;}table,th, td{border: 1px solid black;}td{padding: 6px;}</style><table>'

for person in person_list:
    html_text = html_text + "<tr>" + "<td>" + str(person.number) + "</td>" + "<td>" +person.fname + "</td>"+ "<td>" + person.lname + "</td>"+ "</tr>"
html_text = html_text + '</html>'


#write html to output file
file_out = open("output.html","w")
file_out.write(html_text)
file_out.close()

print 'done'
