def findpayment(loan, r, m):
    '''

    :param loan: a float
    :param r: a float
    :param m:  an int
    :return: a float representing the monthly payment for a mortgage of size loan at a monthly rate of r for m months
    '''

    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    '''
    Abstract class for building different kinds of mortgages
    '''
    def __init__(self, loan, annRate, months):
        '''

        :param loan: a float
        :param annRate: a float
        :param months: an int

        Creates a new mortgage of size loann, duration months and annual interest rate of annRate
        '''
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]  # list of payments that have been made, starting w no payments made
        self.outstanding = [loan]  #
        self.payment = findpayment(loan, self.rate, months)
        self.legend = None  # description of mortgage


    def makePayment(self):
        '''Make a payment'''
        self.paid.append(self.payment)  # append payment to list of payments
        reduction = self.payment - self.outstanding[-1]*self.rate  # remove the last outstanding interest from payment
        self.outstanding.append(self.outstanding[-1] - reduction)  # update the outstanding

    def getTotalPaid(self):
        '''

        :return: Returns total amount paid so far
        '''
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = "Fixed, " + str(round(r*100, 2)) + "%"

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]  # Fixed with points system allows the customer pay a % of the loan(i.e pts)
        self.legend = "Fixed, " + str(round(r*100, 2)) + "%" + str(pts) + "points"

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserRate = teaserRate
        self.teaserMonths = teaserMonths
        self.nextRate = r/12
        self.legend = str(teaserRate*100) + "% for " + str(self.teaserMonths) + " months, then " \
                      + str(round(r*100, 2)) + "%"

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:  # length of list is 1 extra the number of payments
            self.rate = self.nextRate  # bind self's rate to the next rate
            self.payment = findpayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)  # redo payment

        Mortgage.makePayment(self)  # call the makePayment method


# Utilization of Mortgage classes
def compareMortgages(amount, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    total_months = years*12
    fixed_mortgage = Fixed(amount, fixedRate, total_months)  # 1st mortgage : fixed mortgage
    fixed_w_points = FixedWithPts(amount, ptsRate, total_months, pts)  # 2nd mortgage : fixed w points
    two_rate_mortgage = TwoRate(amount, varRate2, total_months, varRate1, varMonths)  # 3rd mortgage : two rate mortgage

    mortgages = [fixed_mortgage, fixed_w_points, two_rate_mortgage]  # making a list of all mortgages

    for month in range(total_months):  # for each month in the range of months
        for mortgage in mortgages:  # and each mortgage in mortgages ...
            mortgage.makePayment()  # make payment for such a mortgage

    for mortgage in mortgages:  # for each mortgage in mortgages ...
        print(mortgage)  # print the mortgage
        print(" Total payments = $" + str(int(mortgage.getTotalPaid())))  # and total amount paid


# compare Mortgage function call
compareMortgages(amount=200000, years=30, fixedRate=0.07, pts=3.25, ptsRate=0.05,
                 varRate1=0.045, varRate2=0.095, varMonths=48)
