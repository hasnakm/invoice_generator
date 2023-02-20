from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('invoice.pdf')


doc.is_paid = True

doc.invoice_info = InvoiceInfo(1884, datetime.now(), datetime.now())  


doc.service_provider_info = ServiceProviderInfo(
    name='Farm Fresh Fruits',
    city='Ernakulam',
    state='Kerala',
)


doc.client_info = ClientInfo(name='Hasna', email='hasna@gmail.com')


doc.add_item(Item('Apple', '', 1, '45'))
doc.add_item(Item('Orange', '', 2, '30'))
doc.add_item(Item('Banana', '', 3, '38'))


doc.set_item_tax_rate(8)  
doc.set_bottom_tip("Thank you for shopping with us!")
doc.finish()