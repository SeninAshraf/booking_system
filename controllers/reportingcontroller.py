class ReportingController:
    def __init__(self, reportingservice):
                        self.reportingservice = reportingservice
    def view_all_transaction(self):
                 return self.reportingservice.view_all_transaction()