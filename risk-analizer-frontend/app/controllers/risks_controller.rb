class RisksController < ApplicationController
  def index
    @risk_score = params[:risk_score]["result"]
  end

  def new
  end

  def create
    puts risk_params
    risk_score_request = RiskScoreRequest.new(risk_params.symbolize_keys)

    puts risk_score_request.to_json

    response = HTTParty.post(
      "http://localhost:4000/api/predict",
      body: risk_score_request.to_json,
      headers: { "Content-Type" => "application/json" }
    )

    if response.code == 200
      @risk_score = JSON.parse(response.body)

      redirect_to risks_path(risk_score: @risk_score)
    else
      puts "ERROR: #{response.code}"
    end
  end

  private

  def risk_params
    permitted_params = [
      :age,
      :annual_income,
      :credit_score,
      :employment_status,
      :education_level,
      :experience,
      :loan_amount,
      :loan_duration,
      :debt_to_income_ratio,
      :number_of_dependents,
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
      :total_debt_to_income_ratio
    ]

    params.permit(permitted_params).to_h
  end
end
