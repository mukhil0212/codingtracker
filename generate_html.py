import pandas as pd

df = pd.read_csv('Coding_Problems_Week_1.csv')
html_output = []

html_output.append("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coding Problems Tracker</title>
    
</head>
<body>
    <h1>Coding Problems Tracker</h1>
    <h2>Week 1</h2>
    <form action="" method="post">
        <table>
            <thead>
                <tr>
                    <th>Problem</th>
                    <th>Difficulty</th>
                    <th>Duration</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
""")

for index, row in df.iterrows():
    status_checked = 'checked' if row['Status'] == 'Completed' else ''
    html_output.append(f"""
                <tr>
                    <td>{row['Problem']}</td>
                    <td>{row['Difficulty']}</td>
                    <td>{row['Duration']}</td>
                    <td><input type="checkbox" name="{index}" {status_checked} onchange="updateStatus({index}, this)"></td>
                </tr>
    """)

html_output.append("""
            </tbody>
        </table>
    </form>
    <script src="script.js"></script>
</body>
</html>
""")

with open('index.html', 'w') as file:
    file.write('\n'.join(html_output))
