# Function to calculate required alloying elements based on target strength and grain size
def calculate_alloying_elements(target_strength, grain_size, base_strength, k_d, k_alloy):
    """
    Calculate the required alloying element weight fractions.
    
    Parameters:
        target_strength (float): Desired yield strength (MPa). This is the target strength you want to achieve in the alloy.
        grain_size (float): Average grain size (µm). The size of the individual grains in the material's microstructure.
        base_strength (float): Strength of the base alloy (MPa). This is the strength of the alloy before any alloying is added.
        k_d (float): Grain boundary strengthening coefficient. A material-specific constant that quantifies how much the grain boundaries contribute to the alloy's strength.
        k_alloy (float): Alloying strengthening factor (MPa per wt%). The factor by which the yield strength increases per unit of alloying element added.
    
    Returns:
        float: Required alloying weight fraction. The amount of alloying element (in wt%) needed to reach the desired strength.
    """
    # Calculate the contribution to the strength from the grain boundary effect (grain refinement)
    grain_effect = k_d * (grain_size ** -0.5)  # Grain size effect on strength
    
    # Calculate the required alloying fraction to achieve the target strength
    required_alloy = (target_strength - base_strength - grain_effect) / k_alloy  # Formula for required alloy fraction
    
    # Ensure that the result is non-negative (i.e., if no alloying is needed, return 0)
    return max(required_alloy, 0)  # Return the alloy fraction, ensuring it's not negative

# Get user inputs for the calculation
target_strength = float(input("Enter target strength (MPa): "))  # Input desired strength
grain_size = float(input("Enter grain size (µm): "))  # Input average grain size
base_strength = float(input("Enter base strength (MPa): "))  # Input strength of base alloy
k_d = float(input("Enter grain boundary strengthening coefficient: "))  # Input grain boundary coefficient
k_alloy = float(input("Enter alloying strengthening factor (MPa per wt%): "))  # Input alloying strengthening factor

# Call the function to calculate the required alloying element weight fraction
required_alloy = calculate_alloying_elements(target_strength, grain_size, base_strength, k_d, k_alloy)

# Output the result
print(f"Required alloying weight fraction: {required_alloy:.2f} wt%")  # Display the calculated alloying fraction