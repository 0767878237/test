document.addEventListener('DOMContentLoaded', function () {
    const statusSelect = document.querySelector('[data-kt-user-table-filter="role"]');
    const applyButton = document.querySelector('[data-kt-user-table-filter="filter"]');
    const resetButton = document.querySelector('[data-kt-user-table-filter="reset"]');
    const rows = document.querySelectorAll('tbody tr');

    function applyFilter() {
        const selectedStatus = statusSelect.value.toLowerCase().trim();
        rows.forEach(row => {
            const rowStatus = (row.getAttribute('data-status') || '').toLowerCase().trim();
            const matchStatus = !selectedStatus || rowStatus === selectedStatus;

            console.log('Row:', rowStatus, 'Match:', matchStatus);

            row.style.display = matchStatus ? '' : 'none';
        });
    }

    function resetFilter() {
        statusSelect.value = '';
        if (window.jQuery) {
            $(statusSelect).trigger('change');
        }

        rows.forEach(row => row.style.display = '');
    }

    applyButton.addEventListener('click', function (e) {
        e.preventDefault();
        applyFilter();
    });

    resetButton.addEventListener('click', function (e) {
        e.preventDefault();
        resetFilter();
    });
});