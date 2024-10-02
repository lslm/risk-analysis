class RiskScoreRequest
  attr_accessor :age,
                :annual_income,
                :credit_score,
                :employment_status,
                :education_level,
                :experience,
                :loan_amount,
                :loan_duration,
                :number_of_dependents,
                :credit_card_utilization_rate,
                :home_ownership_status,
                :monthly_debt_payments,
                :number_of_open_credit_lines,
                :number_of_credit_inquiries,
                :bankruptcy_history,
                :previous_loan_defaults,
                :payment_history,
                :length_of_credit_history,
                :savings_account_balance,
                :checking_account_balance,
                :total_assets,
                :total_liabilities,
                :monthly_income,
                :utility_bills_payment_history,
                :job_tenure,
                :net_worth,
                :base_interest_rate,
                :interest_rate,
                :monthly_loan_payment,
                :total_debt_to_income_ratio,
                :debt_to_income_ratio

  def initialize(params = {})
    # Define os valores padrões para os parâmetros
    defaults = {
      age: 0,
      annual_income: 0,
      credit_score: 0,
      employment_status: "",
      education_level: "",
      experience: 0,
      loan_amount: 0,
      loan_duration: 0,
      number_of_dependents: 0,
      home_ownership_status: "",
      monthly_debt_payments: 0,
      number_of_open_credit_lines: 0,
      number_of_credit_inquiries: 0,
      bankruptcy_history: false,
      previous_loan_defaults: 0,
      payment_history: "",
      length_of_credit_history: 0,
      savings_account_balance: 0,
      checking_account_balance: 0,
      total_assets: 0,
      total_liabilities: 0,
      monthly_income: 0,
      utility_bills_payment_history: "",
      job_tenure: 0,
      net_worth: 0,
      base_interest_rate: 0.0,
      interest_rate: 0.0,
      monthly_loan_payment: 0,
      total_debt_to_income_ratio: 0.0,
      debt_to_income_ratio: 0.0
    }

    # Mescla os parâmetros recebidos com os valores padrão
    options = defaults.merge(params)

    @age = options[:age].to_i
    @annual_income = options[:annual_income].to_i
    @credit_score = options[:credit_score].to_i
    @employment_status = options[:employment_status].to_i
    @education_level = options[:education_level].to_i
    @experience = options[:experience].to_i
    @loan_amount = options[:loan_amount].to_i
    @loan_duration = options[:loan_duration].to_i
    @credit_card_utilization_rate = 0.5
    @number_of_dependents = options[:number_of_dependents].to_i
    @home_ownership_status = options[:home_ownership_status].to_i
    @monthly_debt_payments = options[:monthly_debt_payments].to_i
    @number_of_open_credit_lines = options[:number_of_open_credit_lines].to_i
    @number_of_credit_inquiries = options[:number_of_credit_inquiries].to_i
    @bankruptcy_history = options[:bankruptcy_history] ? 1 : 0
    @previous_loan_defaults = options[:previous_loan_defaults].to_i
    @payment_history = options[:payment_history].to_i
    @length_of_credit_history = options[:length_of_credit_history].to_i
    @savings_account_balance = options[:savings_account_balance].to_i
    @checking_account_balance = options[:checking_account_balance].to_i
    @total_assets = @savings_account_balance + @checking_account_balance
    @total_liabilities = options[:total_liabilities].to_i
    @monthly_income = options[:monthly_income].to_f
    @utility_bills_payment_history = 0.5
    @job_tenure = options[:job_tenure].to_i
    @net_worth = @savings_account_balance + @checking_account_balance
    @base_interest_rate = options[:base_interest_rate].to_f
    @interest_rate = options[:interest_rate].to_f
    @monthly_loan_payment = options[:monthly_loan_payment].to_f
    @total_debt_to_income_ratio = @loan_amount / @annual_income
    @debt_to_income_ratio = @total_debt_to_income_ratio
  end

  # Método auxiliar para converter snake_case em PascalCase
  def pascal_case(str)
    str.split("_").map(&:capitalize).join
  end

  def to_json
    # Cria um hash com as chaves em PascalCase
    data = {
      age: @age,
      annual_income: @annual_income,
      credit_score: @credit_score,
      employment_status: @employment_status,
      education_level: @education_level,
      experience: @experience,
      loan_amount: @loan_amount,
      loan_duration: @loan_duration,
      number_of_dependents: @number_of_dependents,
      home_ownership_status: @home_ownership_status,
      monthly_debt_payments: @monthly_debt_payments,
      number_of_open_credit_lines: @number_of_open_credit_lines,
      number_of_credit_inquiries: @number_of_credit_inquiries,
      bankruptcy_history: @bankruptcy_history,
      previous_loan_defaults: @previous_loan_defaults,
      payment_history: @payment_history,
      length_of_credit_history: @length_of_credit_history,
      savings_account_balance: @savings_account_balance,
      checking_account_balance: @checking_account_balance,
      total_assets: @total_assets,
      total_liabilities: @total_liabilities,
      monthly_income: @monthly_income,
      utility_bills_payment_history: @utility_bills_payment_history,
      job_tenure: @job_tenure,
      net_worth: @net_worth,
      base_interest_rate: @base_interest_rate,
      interest_rate: @interest_rate,
      monthly_loan_payment: @monthly_loan_payment,
      total_debt_to_income_ratio: @total_debt_to_income_ratio,
      debt_to_income_ratio: @debt_to_income_ratio,
      credit_card_utilization_rate: @credit_card_utilization_rate
    }

    # Transforma as chaves do hash em PascalCase
    pascal_case_data = data.transform_keys { |key| pascal_case(key.to_s) }

    pascal_case_data.to_json
  end
end
