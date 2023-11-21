<!DOCTYPE html>
<html>
<head>
    <title>Chart.js Example</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Chart.js Example</h1>
    <canvas id="myChart" width="400" height="200"></canvas>

    <script>
        var data = {{ data_json|tojson|safe }};  // Pythonから渡されたJSONデータ

        var labels = data.map(item => item.label);
        var values = data.map(item => item.value);

        var ctx = document.getElementById("myChart").getContext("2d");
        var myChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Sample Data",
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1,
                    data: values,
                }],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    </script>
</body>
</html>
