using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using Andersc.AlgorithmInCs.Common.Validation;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    internal class Recipe
    {
        [Required]
        public string Name { get; set; }

        [PositiveInteger]
        public int Age { get; set; }

        [NotEmpty]
        public List<string> Materials { get; set; }
    }

    public static class ValidationExtensions
    {
        public static bool TryValidate(this object obj, out List<ValidationResult> results)
        {
            var context = new ValidationContext(obj, serviceProvider: null, items: null);
            results = new List<ValidationResult>();
            return Validator.TryValidateObject(
                obj, context, results,
                validateAllProperties: true
            );
        }
    }

    [TestFixture]
    public class TestValidator
    {
        [TestCase]
        public void TestValidators()
        {
            var recipe = new Recipe();
            List<ValidationResult> results;

            var isValid = recipe.TryValidate(out results);
            if (!isValid)
            {
                foreach (var validationResult in results)
                {
                    Console.WriteLine(validationResult.ErrorMessage);
                }
            }
        }
    }
}
