from faker import Faker

faker = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, eMail_address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.eMail_address = eMail_address

    @property
    def label_length(self):
        return len(self.name + ' ' + self.surname)

    def contact(self):
        print(
            f"Dialing {self.phone}"
            f" and calling {self.name} {self.surname}"
        )

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.eMail_address}'


class BusinessContact(BaseContact):
    def __init__(self, company, position, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.work_phone = work_phone

    @property
    def label_length(self):
        return len(self.name + ' ' + self.surname)

    def contact(self):
        print(
            f"Dialing {self.work_phone}"
            f" and calling {self.name} {self.surname}"
        )

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.work_phone}'


def create_contacts(business_card, number):
    address_book = []
    if business_card == 'BaseContact':
        for contact in range(number):
            contact = BaseContact(
                name = faker.first_name(),
                surname = faker.last_name(),
                phone = faker.phone_number(),
                eMail_address = faker.email()
            )
            address_book.append(contact)
    elif business_card == 'BusinessContact':
        for contact in range(number):
            contact = BusinessContact(
                name = faker.first_name(),
                surname = faker.last_name(),
                phone = faker.phone_number(),
                eMail_address = faker.email(),
                company = faker.company(),
                position = faker.job(),
                work_phone = faker.phone_number()
            )
            address_book.append(str(contact))
    else:
        raise ValueError(
            f"Business Card name: {business_card} "
            f"is neither 'BaseContact' nor 'BusinessContact'")
    return address_book
    

personal_data = create_contacts('BusinessContact', 10)

print(personal_data)
