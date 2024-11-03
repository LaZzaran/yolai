using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace BTK.Controllers
{
    public class MentorController : Controller
    {
       BtkContext _context = new BtkContext();

      
        public IActionResult Mesajlaşma()
        {
            return View();
        }
         
          public async Task<IActionResult> Randevu(string subject = null)
            {
                var teachers = await _context.Mentors
                    .Where(t => string.IsNullOrEmpty(subject) || t.MentorArea == subject)
                    .ToListAsync();

                return View(teachers);
            }
        [HttpGet]
        public async Task<IActionResult> GetMentorEmail(int mentorId)
        {
            var mentor = await _context.Mentors.FindAsync(mentorId);
            if (mentor == null)
            {
                return NotFound("Mentor bulunamadı.");
            }

            return Ok(mentor.Mentormail); // Mentorun e-posta adresini döner
        }
    }
    }



