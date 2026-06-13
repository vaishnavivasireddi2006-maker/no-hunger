// Analytics Charts Script - Community Food Waste Rescue Network

document.addEventListener('DOMContentLoaded', function() {
    // Check if we are on the analytics dashboard page
    const trendsCtx = document.getElementById('donationTrendChart');
    const categoryCtx = document.getElementById('categoryChart');
    const rescueCtx = document.getElementById('rescueRateChart');

    if (trendsCtx || categoryCtx || rescueCtx) {
        fetch('/api/analytics')
            .then(response => response.json())
            .then(data => {
                if (trendsCtx && data.monthly_trends) {
                    renderTrendsChart(trendsCtx, data.monthly_trends);
                }
                if (categoryCtx && data.categories) {
                    renderCategoryChart(categoryCtx, data.categories);
                }
                if (rescueCtx && data.rescue_stats) {
                    renderRescueChart(rescueCtx, data.rescue_stats);
                }
            })
            .catch(error => console.error('Error fetching analytics data:', error));
    }
});

function renderTrendsChart(ctx, trendData) {
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: trendData.labels,
            datasets: [{
                label: 'Food Rescued (kg)',
                data: trendData.values,
                borderColor: '#2e7d32',
                backgroundColor: 'rgba(46, 125, 50, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

function renderCategoryChart(ctx, categoryData) {
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: categoryData.labels,
            datasets: [{
                data: categoryData.values,
                backgroundColor: [
                    '#2e7d32', // Medium Green
                    '#e65100', // Primary Orange
                    '#4caf50', // Light Green
                    '#ff9800', // Accent Orange
                    '#1e5631', // Dark Green
                    '#ffb74d'  // Light Orange
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        boxWidth: 12,
                        padding: 15
                    }
                }
            }
        }
    });
}

function renderRescueChart(ctx, rescueData) {
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: rescueData.labels,
            datasets: [{
                label: 'Donations',
                data: rescueData.values,
                backgroundColor: [
                    '#2e7d32', // Rescued/Completed
                    '#e65100', // Available/Pending
                    '#9e9e9e'  // Cancelled/Expired
                ],
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}
