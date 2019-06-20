import re

class EchiumTree:
    def __init__(self, data):
        self.raw_data = data
        self.root = ''
        self.variables = {'':1}
        self.contents = {}
        self.commands = {}
        self.output = ''
    
    def parse(self):
        ''' populates contents and variables '''
        # first let's find variables
        variables = re.findall(r'var +(\w+) += +(\d+) *;',self.raw_data)
        for var in variables:
            self.variables[var[0]] = int(var[1])
        contents = re.findall(r"content +(\w+) += +'(.+)'",self.raw_data)
        for cont in contents:
            file_id = cont[0]
            file_name = cont[1]
            file_handle = open('src/'+file_name)
            self.contents[file_id]=file_handle.read()
        render_box = re.compile(r"render +{(.*)}",
         flags=re.DOTALL).search(self.raw_data)[1]
        self.root = render_box
        raw_commands = re.findall(r"(@\w+\*(\w*);)",render_box)
        actual_commands = {}
        for com in raw_commands:
            content_name = com[0]
            content_repeat_variable = com[1]
            repeat = self.variables[content_repeat_variable]
            actual_commands[content_name] = repeat
        self.commands = actual_commands
                    
        return True

    
    def render(self):
        ''' compiles the output string '''
        ready_content = {}
        for com_id,com_rep in self.commands.items():
            content_id = re.search(r"@(\w+)*\w*",com_id)[1]
            content_content = self.contents[content_id]
            repeat = com_rep
            ready_content[com_id] = content_content*repeat

        # beginning compilation
        self.output = self.root
        for token,content in ready_content.items():
            self.output = self.output.replace(token,content)
        return self.output