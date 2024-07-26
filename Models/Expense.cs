using System.ComponentModel.DataAnnotations;

namespace Expense_App.Models
{
    public class Expense
    {
        private int Id { get; set; }
        private decimal Value { get; set; }
        [Required]

        private string? Description { get; set; }
    }
}
