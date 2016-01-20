using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Andersc.AlgorithmInCs.Common.Validation
{
    public class NotEmptyAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            var enumerable = value as IEnumerable<object>;

            if (enumerable.IsNotEmpty())
            {
                return ValidationResult.Success;
            }
            return new ValidationResult(string.Format("{0} cannot be empty.", validationContext.DisplayName));
        }
    }
}