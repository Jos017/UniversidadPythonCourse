class File_manager:
    def __init__(self, name):
        self.name = name

    # This method executes when "with" is used and the file is opened
    def __enter__(self):
        print('Get the resource'.center(50, '-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name

    # This method executes when the file is closed
    def __exit__(self, exception_type, exception_value, error_trace):
        print('Closing the resource'.center(50, '-'))
        if self.name:
            self.name.close()
