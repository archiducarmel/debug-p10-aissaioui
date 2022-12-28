# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

class BookingDetails:
    def __init__(
        self,
        destination: str = None,
        origin: str = None,
        budget: int = None,
        start_date: str = None,
        end_date: str = None,
        unsupported_airports=None,
        turns: list = []
    ):
        if unsupported_airports is None:
            unsupported_airports = []
        self.destination = destination
        self.origin = origin
        self.budget = budget
        self.start_date = start_date
        self.end_date = end_date
        self.unsupported_airports = unsupported_airports
        self.turns = turns

    def get_details(self):
        return str({
            "destination":self.destination,
            "origin":self.origin,
            "from_date":self.start_date,
            "to_date:":self.end_date,
            "budget:":self.budget
        })

    def to_dict(self):
    
        try:
            start_date = self.start_date[-1].value
        except :
            try:
                start_date = self.start_date[0].value
            except:
                start_date = self.start_date
            
            
        try:
            end_date = self.end_date[-1].value
        except :
            try:
                end_date = self.end_date[0].value
            except:
                end_date = self.end_date
        return {
            "dst_city":self.destination.upper(),
            "or_city":self.origin.upper(),
            "str_date":start_date,
            "end_date":end_date,
            "budget":self.budget
        }
        
    def check_budget(self,budget):
        try:
            budget = float(budget)
            if budget > 0 and budget < 10000:
                return True
            else:
                return False
        except:
            return False

    def check_date(self,date):
        return True
    
    def reset_turns(self):
        self.turns = []