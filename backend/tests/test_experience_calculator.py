from backend.experience_engine.experience_calculator import ExperienceCalculator

calculator = ExperienceCalculator()

examples = [

    ("2020-08", "Present"),

    ("2019-01", "2022-05"),

    ("2023-01", "2024-07")

]

for start, end in examples:

    result = calculator.calculate(

        start,

        end

    )

    print()

    print("Start :", start)

    print("End   :", end)

    print(result)