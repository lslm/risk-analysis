from pydantic import BaseModel

class PredictionRequest(BaseModel):
    """Modelo de Request que recebe os dados para a predição
    """
    Age:                             int
    AnnualIncome:                    int
    CreditScore:                     int
    EmploymentStatus:                int
    EducationLevel:                  int
    Experience:                      int
    LoanAmount:                      int
    LoanDuration:                    int
    NumberOfDependents:              int
    HomeOwnershipStatus:             int
    MonthlyDebtPayments:             int
    CreditCardUtilizationRate:     float
    NumberOfOpenCreditLines:         int
    NumberOfCreditInquiries:         int
    DebtToIncomeRatio:             float
    BankruptcyHistory:               int
    PreviousLoanDefaults:            int
    PaymentHistory:                  int
    LengthOfCreditHistory:           int
    SavingsAccountBalance:           int
    CheckingAccountBalance:          int
    TotalAssets:                     int
    TotalLiabilities:                int
    MonthlyIncome:                 float
    UtilityBillsPaymentHistory:    float
    JobTenure:                       int
    NetWorth:                        int
    BaseInterestRate:              float
    InterestRate:                  float
    MonthlyLoanPayment:            float
    TotalDebtToIncomeRatio:        float

class PredictionResponse(BaseModel):
    """Modelo de Response com os dados da predição
    """
    result: float