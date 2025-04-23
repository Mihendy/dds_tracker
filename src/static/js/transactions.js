let allCategories = [];
let allSubcategories = [];

function deleteTransaction(pk, csrf_token) {
    if (!confirm("Вы уверены, что хотите удалить эту запись?")) return;

    fetch(`/transactions/${pk}/delete/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok) {
                document.getElementById(`transaction-row-${pk}`).remove();
            } else {
                alert("Ошибка при удалении.");
            }
        });
}

function updateSelect(selectId, items) {
    const select = document.getElementById(selectId);
    select.innerHTML = '<option value="">----</option>';  // дефолтная опция

    items.forEach(item => {
        const option = document.createElement("option");
        option.value = item.pk;
        option.textContent = item.name;
        select.appendChild(option);
    });
}

function updateCategoriesAndSubcategories(typeId = null) {
    if (!typeId) {
        updateSelect("id_category", allCategories);
        updateSelect("id_subcategory", allSubcategories);
        return;
    }

    fetch(`/transactions/get_categories_by_type/${typeId}/`)
        .then(response => response.json())
        .then(data => {
            updateSelect("id_category", data.categories);
            updateSelect("id_subcategory", data.subcategories);
        });
}

document.addEventListener("DOMContentLoaded", function () {
    // Сохраняем все доступные опции изначально
    allCategories = Array.from(document.getElementById("id_category").options)
        .filter(opt => opt.value)
        .map(opt => ({ pk: opt.value, name: opt.textContent }));

    allSubcategories = Array.from(document.getElementById("id_subcategory").options)
        .filter(opt => opt.value)
        .map(opt => ({ pk: opt.value, name: opt.textContent }));

    const selectedTypeId = document.getElementById("id_type").value;
    const selectedCategoryId = document.getElementById("id_category").value;
    const selectedSubcategoryId = document.getElementById("id_subcategory").value;

    if (!selectedCategoryId && !selectedSubcategoryId) {
        updateCategoriesAndSubcategories(selectedTypeId);
    }

    document.getElementById("id_type").addEventListener("change", function () {
        const typeId = this.value;
        updateCategoriesAndSubcategories(typeId);
    });
});
