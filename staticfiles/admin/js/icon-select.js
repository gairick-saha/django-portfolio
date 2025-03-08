const dropdown = document.getElementById("iconDropdown");

dropdown.addEventListener("change", function () {
  const selectedOption = this.options[this.selectedIndex];
  const iconClass = selectedOption.getAttribute("data-icon");

  // Remove previous icons
  const existingIcon = this.querySelector("i");
  if (existingIcon) {
    existingIcon.remove();
  }

  // Create and prepend new icon
  const icon = document.createElement("i");
  icon.className = iconClass;
  this.insertBefore(icon, this.firstChild);
});

// Trigger initial icon display
dropdown.dispatchEvent(new Event("change"));
