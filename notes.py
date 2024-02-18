import datetime

class Notes(object):

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.date = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')


    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date_change(self):
        return self.date

    def get_string(self):
        return (f"Title: {self.title};\n"
                f"Body: {self.body};\n"
                f"Date last change: {self.date};\n\n")
