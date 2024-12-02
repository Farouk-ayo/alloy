// Function to calculate the required alloying weight fraction
function calculateAlloyingElements(
  targetStrength,
  grainSize,
  baseStrength,
  k_d,
  k_alloy
) {
  // Calculate the contribution to the strength from the grain boundary effect (grain refinement)
  const grainEffect = k_d * grainSize ** -0.5; // Grain size effect on strength

  // Calculate the required alloying fraction to achieve the target strength
  const requiredAlloy = (targetStrength - baseStrength - grainEffect) / k_alloy; // Formula for required alloy fraction

  // Ensure the result is non-negative (i.e., if no alloying is needed, return 0)
  return Math.max(requiredAlloy, 0); // Return the alloy fraction, ensuring it's not negative
}

// Event listener for the form submission
document
  .getElementById("calculator-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the user input values
    const targetStrength = parseFloat(
      document.getElementById("target-strength").value
    );
    const grainSize = parseFloat(document.getElementById("grain-size").value);
    const baseStrength = parseFloat(
      document.getElementById("base-strength").value
    );
    const k_d = parseFloat(document.getElementById("k-d").value);
    const k_alloy = parseFloat(document.getElementById("k-alloy").value);

    // Validate inputs
    if (
      isNaN(targetStrength) ||
      isNaN(grainSize) ||
      isNaN(baseStrength) ||
      isNaN(k_d) ||
      isNaN(k_alloy)
    ) {
      alert("Please enter valid numbers for all fields.");
      return;
    }

    // Calculate the required alloying weight fraction
    const requiredAlloy = calculateAlloyingElements(
      targetStrength,
      grainSize,
      baseStrength,
      k_d,
      k_alloy
    );

    // Display the result
    document.getElementById(
      "alloy-weight"
    ).textContent = `${requiredAlloy.toFixed(2)} wt%`;
  });
