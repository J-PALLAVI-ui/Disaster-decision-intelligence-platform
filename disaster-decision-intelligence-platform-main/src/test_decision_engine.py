from decision_engine import DecisionEngine

result = DecisionEngine.analyze(
    magnitude=6.4,
    depth=15,
    temperature=31,
    humidity=82
)

print(result)