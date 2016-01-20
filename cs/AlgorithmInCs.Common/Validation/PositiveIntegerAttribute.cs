using System.ComponentModel.DataAnnotations;

namespace Andersc.AlgorithmInCs.Common.Validation
{
    public class PositiveIntegerAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            var val = (int) value;
            if (val > 0)
            {
                return ValidationResult.Success;
            }
            return new ValidationResult(string.Format("{0} should be positive", validationContext.DisplayName));
        }
    }
}