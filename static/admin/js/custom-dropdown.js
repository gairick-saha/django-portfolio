document.addEventListener("DOMContentLoaded", function () {
  const dropdowns = document.querySelectorAll(".searchable-dropdown");

  dropdowns.forEach((dropdown) => {
    const fieldName = dropdown.dataset.fieldName;
    const selectBtn = dropdown.querySelector(".select-btn");
    const dropdownContent = dropdown.querySelector(
      ".searchable-dropdown-content"
    );
    const searchInput = dropdown.querySelector("input[type='text']");
    const options = dropdown.querySelectorAll(".dropdown-options li");
    const hiddenInput = document.querySelector(
      `input[name="${fieldName}"][type="hidden"]`
    );

    dropdownContent.style.maxHeight = "300px";
    dropdownContent.style.overflowY = "auto";

    calculateMaxWidth(dropdown, options, selectBtn);

    function calculateMaxWidth(dropdown, options, selectBtn) {
      const tempDiv = document.createElement("div");
      tempDiv.style.position = "absolute";
      tempDiv.style.visibility = "hidden";
      tempDiv.style.whiteSpace = "nowrap";

      const firstOptionP = options[0]?.querySelector("p");
      if (firstOptionP) {
        tempDiv.style.fontSize = window.getComputedStyle(firstOptionP).fontSize;
        tempDiv.style.fontFamily =
          window.getComputedStyle(firstOptionP).fontFamily;
      }

      document.body.appendChild(tempDiv);

      let maxWidth = 0;

      options.forEach((option) => {
        const text = option.querySelector("p").textContent;
        tempDiv.textContent = text;
        const textWidth = tempDiv.offsetWidth;

        const hasIcon = option.querySelector("i") !== null;
        const iconWidth = hasIcon ? 50 : 0;
        const totalWidth = textWidth + iconWidth + 40;

        if (totalWidth > maxWidth) {
          maxWidth = totalWidth;
        }
      });

      document.body.removeChild(tempDiv);

      maxWidth += 40;

      const minWidth = 200;
      maxWidth = Math.max(maxWidth, minWidth);

      selectBtn.style.width = maxWidth + "px";
      dropdown.querySelector(".searchable-dropdown-content").style.width =
        maxWidth + "px";
    }

    selectBtn.addEventListener("click", function () {
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        document
          .querySelectorAll(".searchable-dropdown-content")
          .forEach((content) => {
            content.style.display = "none";
          });

        dropdownContent.style.display = "block";
        searchInput.focus();
      }
    });

    document.addEventListener("click", function (e) {
      if (!dropdown.contains(e.target)) {
        dropdownContent.style.display = "none";
      }
    });

    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();

      options.forEach((option) => {
        const text = option.querySelector("p").textContent.toLowerCase();
        const value = option.getAttribute("value").toLowerCase();

        if (
          text.includes(searchTerm) ||
          (value && value.includes(searchTerm))
        ) {
          option.style.display = "flex";
        } else {
          option.style.display = "none";
        }
      });
    });

    searchInput.addEventListener("keydown", function (e) {
      const visibleOptions = Array.from(options).filter(
        (opt) => opt.style.display !== "none"
      );
      const highlighted = dropdown.querySelector(
        ".dropdown-options li.highlighted"
      );

      if (e.key === "ArrowDown") {
        e.preventDefault();
        if (!highlighted) {
          if (visibleOptions.length > 0) {
            visibleOptions[0].classList.add("highlighted");
            visibleOptions[0].scrollIntoView({ block: "nearest" });
          }
        } else {
          const currentIndex = visibleOptions.indexOf(highlighted);
          highlighted.classList.remove("highlighted");

          if (currentIndex < visibleOptions.length - 1) {
            visibleOptions[currentIndex + 1].classList.add("highlighted");
            visibleOptions[currentIndex + 1].scrollIntoView({
              block: "nearest",
            });
          } else {
            visibleOptions[0].classList.add("highlighted");
            visibleOptions[0].scrollIntoView({ block: "nearest" });
          }
        }
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        if (!highlighted) {
          if (visibleOptions.length > 0) {
            visibleOptions[visibleOptions.length - 1].classList.add(
              "highlighted"
            );
            visibleOptions[visibleOptions.length - 1].scrollIntoView({
              block: "nearest",
            });
          }
        } else {
          const currentIndex = visibleOptions.indexOf(highlighted);
          highlighted.classList.remove("highlighted");

          if (currentIndex > 0) {
            visibleOptions[currentIndex - 1].classList.add("highlighted");
            visibleOptions[currentIndex - 1].scrollIntoView({
              block: "nearest",
            });
          } else {
            visibleOptions[visibleOptions.length - 1].classList.add(
              "highlighted"
            );
            visibleOptions[visibleOptions.length - 1].scrollIntoView({
              block: "nearest",
            });
          }
        }
      } else if (e.key === "Enter" && highlighted) {
        e.preventDefault();
        highlighted.click();
      } else if (e.key === "Escape") {
        dropdownContent.style.display = "none";
      }
    });

    options.forEach((option) => {
      option.addEventListener("click", function () {
        const value = this.getAttribute("value");
        const label = this.querySelector("p").textContent;

        const icon = this.querySelector("i");
        const iconHtml = icon ? icon.outerHTML : "";

        if (iconHtml && fieldName == "logo") {
          let contentContainer = selectBtn.querySelector(".content-container");
          if (!contentContainer) {
            contentContainer = document.createElement("div");
            contentContainer.className = "content-container";
            contentContainer.style.display = "flex";
            contentContainer.style.alignItems = "center";
            contentContainer.style.gap = "12px";

            contentContainer.innerHTML = `
              ${fieldName == "logo" ? iconHtml : ""}
              <span style="font-size: 14px;">${label}</span>
            `;

            const oldSpan = selectBtn.querySelector(
              "span:not(.content-container span)"
            );
            if (oldSpan) {
              selectBtn.replaceChild(contentContainer, oldSpan);
            } else {
              selectBtn.insertBefore(contentContainer, selectBtn.firstChild);
            }
          } else {
            contentContainer.innerHTML = `
              ${fieldName == "logo" ? iconHtml : ""}
              <span style="font-size: 14px;">${label}</span>
            `;
          }

          const containerIcon = contentContainer.querySelector("i");
          if (containerIcon) {
            containerIcon.style.fontSize = "40px";
            containerIcon.style.width = "40px";
            containerIcon.style.height = "40px";
            containerIcon.style.display = "flex";
            containerIcon.style.alignItems = "center";
            containerIcon.style.justifyContent = "center";
            containerIcon.classList.add("colored");
          }
        } else {
          let contentContainer = selectBtn.querySelector(".content-container");
          if (contentContainer) {
            contentContainer.remove();
          }

          const span =
            selectBtn.querySelector("span:not(.content-container span)") ||
            document.createElement("span");
          span.textContent = label;

          if (!span.parentNode) {
            selectBtn
              .querySelectorAll("span:not(.content-container span)")
              .forEach((s) => s.remove());

            selectBtn.insertBefore(span, selectBtn.firstChild);
          }
        }

        if (hiddenInput) {
          hiddenInput.value = value;
          console.log(`Updated hidden input ${fieldName} with value: ${value}`);
        } else {
          console.error(`Hidden input for ${fieldName} not found!`);
        }

        options.forEach((opt) => opt.classList.remove("selected"));
        this.classList.add("selected");

        dropdownContent.style.display = "none";

        searchInput.value = "";
        options.forEach((opt) => (opt.style.display = "flex"));

        dropdown
          .querySelectorAll(".dropdown-options li.highlighted")
          .forEach((el) => el.classList.remove("highlighted"));

        if (hiddenInput) {
          const event = new Event("change", { bubbles: true });
          hiddenInput.dispatchEvent(event);
        }
      });
    });

    if (hiddenInput && hiddenInput.value) {
      const preselectedValue = hiddenInput.value;
      const selectedOption = Array.from(options).find(
        (opt) => opt.getAttribute("value") === preselectedValue
      );

      if (selectedOption) {
        selectedOption.click();
      }
    }
  });
});
