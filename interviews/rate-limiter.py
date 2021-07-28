from datetime import datetime
rates = {
    1 : []
}


def rateLimiter(customer_id):
    rate = 10
    now = datetime.now()

    # current_time = now.strftime("%H:%M:%S")

    # if (len(rates[customer_id])+1)>10:
    #     return False
    #
    # else:
    #     rates[customer_id].append(now)
    #     return True

    if len(rates[customer_id])>0:
        last_access = rates[customer_id][0]

        last_hour = int(last_access.strftime("%H"))
        last_min = int(last_access.strftime("%M"))

        current_hour = int(now.strftime("%H"))
        current_min = int(now.strftime("%M"))

        status = True

        rates[customer_id].append(now)

        if (len(rates[customer_id])) > rate:
            rates[customer_id].pop(0)
            status = False

        if current_hour>last_hour:
            status = True

        if current_min>last_min:
            status = True

        return status

    else:
        rates[customer_id].append(now)

    return True


for i in range(12):
    print(rateLimiter(1))



