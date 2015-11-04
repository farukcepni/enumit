enumit
====
Enumeration class for python. 


Basic Usage
====

    class Status(Enum):
        WAITING = Enum.Field('waiting', 'Waiting')
        APPROVED = Enum.Field('approved', 'Approved')


    >> print Status.APPROVED
    >> approved
    
    >> print Status['approved']
    >> Approved

    # choices, values and names will be in defined order.
    >> print Status.choices()
    >> [('approved', 'Approved'), ('denied', 'Denied')]

    >> print Status.values()
    >> ['approved', 'denied']

    >> print Status.names()
    >> ['Approved', 'Denied']
    
    >> Status.APPROVED = 'new_approved_value'
    # raise ValueError('Enum field can not be changed.')
    
    >> del Status.APPROVED
    # raise ValueError('Enum field can not be deleted.')

    >> 'approved' in Status
    >> True

    >> len(Status)
    >> 2
