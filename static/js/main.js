// Main UI Script - Community Food Waste Rescue Network

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss Bootstrap Alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Form Client-side Validation helper
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Update Freshness indicators and countdown timers dynamically
    updateFreshnessTimers();
    setInterval(updateFreshnessTimers, 60000); // Update every minute
});

/**
 * Calculates remaining hours and updates freshness badge style/text
 */
function updateFreshnessTimers() {
    const badges = document.querySelectorAll('.freshness-timer-badge');
    badges.forEach(badge => {
        const expiryStr = badge.getAttribute('data-expiry');
        if (!expiryStr) return;

        const expiryDate = new Date(expiryStr);
        const now = new Date();
        const diffMs = expiryDate - now;

        let badgeClass = 'freshness-critical';
        let text = 'Expired';

        if (diffMs > 0) {
            const diffHours = diffMs / (1000 * 60 * 60);
            
            if (diffHours > 6) {
                badgeClass = 'freshness-fresh';
                text = `Fresh (${Math.round(diffHours)}h left)`;
            } else if (diffHours > 2) {
                badgeClass = 'freshness-moderate';
                text = `Expiring soon (${Math.round(diffHours)}h left)`;
            } else {
                badgeClass = 'freshness-critical';
                const diffMins = Math.round(diffMs / (1000 * 60));
                text = `Urgent (${diffMins}m left)`;
            }
        }

        // Apply badge styling classes
        badge.className = `freshness-indicator ${badgeClass} freshness-timer-badge`;
        badge.textContent = text;
    });
}
