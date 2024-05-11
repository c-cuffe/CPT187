# Create patient class
class Patient:
    # Take in attributes
    def __init__(self, first, middle, last, address, city, state, zip, phone, em_name, em_phone):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone
        self.__em_name = em_name
        self.__em_phone = em_phone

    # Create mutators
    def set_first(self, first):
        if first.isalpha():
            self.__first = first

    def set_middle(self, middle):
        if middle.isalpha():
            self.__middle = middle

    def set_last(self, last):
        if last.isalpha():
            self.__last = last

    def set_city(self, city):
        if city.isalpha():
            self.__city = city

    def set_zip(self, zip):
        if zip.isnumeric():
            self.__zip = zip

    def set_phone(self, phone):
        if phone.isnumeric():
            self.__phone = phone

    def set_em_name(self, em_name):
        if em_name.isalpha():
            self.__first = em_name

    def set_em_phone(self, em_phone):
        if em_phone.isnumeric():
            self.__em_phone = em_phone

    # Create accessors
    def get_first(self, first):
        return self.__first

    def get_middle(self, middle):
        return self.__middle

    def get_last(self, last):
        return self.__last

    def get_city(self, city):
        return self.__city

    def get_zip(self, zip):
        return self.__zip

    def get_phone(self, phone):
        return self.__phone

    def get_em_name(self, em_name):
        return self.__first

    def get_em_phone(self, em_phone):
        return self.__em_phone

    def __str__(self):
        return "Patient Info\nName: {} {} {}\nAddress {} {}, {} {}\nContact Info: {}\nEmergency Contact Info: {} {}" \
            .format(self.__first, self.__middle, self.__last, self.__address, self.__city,
                    self.__state, self.__zip, self.__phone, self.__em_name, self.__em_phone)


# Create Procedure class
class Procedure:
    # Take in attributes
    def __init__(self, proc_name, date, doc, charges):
        self.__proc_name = proc_name
        self.__date = date
        self.__doc = doc
        self.__charges = charges

    # Create mutators
    def set_proc_name(self, proc_name):
        self.__proc_name = proc_name

    def set_date(self, date):
        self.__date = date

    def set_doc(self, doc):
        self.__doc = doc

    def set_charges(self, charges):
        self.__charges = charges

    # Create accessors
    def get_proc_name(self):
        return self.__proc_name

    def get_date(self):
        return self.__date

    def get_doc(self):
        return self.__doc

    def get_charges(self):
        return self.__charges


def main():
    # Create instance of patient class
    patient = Patient("Jane", "A.", "Doe", "1234 Cherry Lane",
                      "Little River", "SC", 29566, 8431234567, "John Doe", 8434567890)
    print(patient)
    # Create three instances of procedure class
    proc1 = Procedure("Physical Exam", "4/16/2023", "Dr. Irvine", 250)
    proc2 = Procedure("X-ray", "4/16/2023", "Dr. Jamison", 500)
    proc3 = Procedure("Blood test", "4/16/2023", "Dr. Smith", 200)
    # Create headers and display data
    print("Procedure #1\t\t\t\t\tProcedure #2\t\t\t\t\tProcedure #3")
    print("Procedure Name: {}\tProcedure Name: {}\t\t\tProcedure Name: {}".format(
        proc1.get_proc_name(), proc2.get_proc_name(), proc3.get_proc_name()))
    print("Date: {}\t\t\t\t\tDate: {}\t\t\t\t\tDate: {}".format(
        proc1.get_date(), proc2.get_date(), proc3.get_date()))
    print("Practitioner: {}\t\tPractitioner: {}\t\tPractitioner: {}".format(
        proc1.get_doc(), proc2.get_doc(), proc3.get_doc()))
    print("Charge: {:.2f}\t\t\t\t\tCharge: {:.2f}\t\t\t\t\tCharge: {:.2f}".format(
        proc1.get_charges(), proc2.get_charges(), proc3.get_charges()))
    total_charges = (proc1.get_charges() + proc2.get_charges() + proc3.get_charges())
    print("Total Charges: ${:.2f}".format(total_charges))


if __name__ == "__main__":
    main()
