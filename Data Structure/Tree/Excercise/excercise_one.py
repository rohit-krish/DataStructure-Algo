'''
QUESTION 1.
Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class.
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
'''


class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, which):
        if which == 'name':
            data = self.name
        elif which == 'designation':
            data = self.designation
        elif which == 'both':
            data = '{} ({})'.format(self.name, self.designation)
        else:
            raise Exception('Invalid Argument')

        spaces = '  ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix+data if self.get_level() == 1 else '',
              end='\n' if self.get_level() == 1 else '\r')

        if self.children:
            for child in self.children:
                child.print_tree(which)


if __name__ == '__main__':
    ceo = TreeNode('Nilupul', 'CEO')
    cto = TreeNode('Chinmay', 'CTO')
    hr_head = TreeNode('Gels', 'HR Head')
    infrastructure_head = TreeNode('Vishwa', 'Infrastructure Head')
    application_head = TreeNode('Aamir', 'Application Head')
    cloud_manager = TreeNode('Dhaval', 'Cloud Manager')
    app_manager = TreeNode('Abhijit', 'App Manager')
    recruitment_manager = TreeNode('Peter', 'Recruitment Manager')
    policy_manager = TreeNode('Waqas', 'Policy Manager')

    infrastructure_head.add_child(cloud_manager)
    infrastructure_head.add_child(app_manager)

    cto.add_child(infrastructure_head)
    cto.add_child(application_head)

    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    ceo.print_tree('both')
