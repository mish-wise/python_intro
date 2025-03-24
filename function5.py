#TCO3V7DGN3 Confirmed. Ksh3,000 sent to FRANCIS KINUNGI ON 24/3/25 at 8:30AM.
def extract_amount(mpesa_message):
    index_ksh= mpesa_message.index("Ksh")
    index_sent=mpesa_message.index("sent")
    amount=mpesa_message[index_ksh: index_sent]

    print(amount)

def extract_date(mpesa_message):
    index_on=mpesa_message.index(" on ")
    index_at=mpesa_message.index(" at ")
    date=mpesa_message[index_on:index_at]
    date=date.replace("on","")
    date=date.strip()#remove whitespace
    print(date)



message_1="TCO3V7DGN3 Confirmed. Ksh3,000 sent to FRANCIS KINUNGI ON 24/3/25 at 8:30AM."
extract_amount(message_1)
