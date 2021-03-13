## Data Analytics Shopee Code League

#### Description Data
- Order ID -> Represent transaction
- Id in Ticket ID -> made to Shopee Customer Service
- All phone number are stored without country code and the country code can be ignored (mungkin bisa di filter?)
- Contact represent the number of times user reached out particular ticket (email, call, livechat, etc)
- If a value is NA means no record

#### Example
```
Id : 0
Email : john@gmail.com
Phone : NA
Order ID : 12345678
Contacts : 5 # berarti 5 kali ngehubungi
```

#### Submission Format

Two columns required:
- ticket_id
- ticket_trace/contact
    - Format: (tickets in ascending order), (total contact)

Your submission should have **500.000 rows** excluding headers, each with 2 columns
