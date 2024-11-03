using BTK.DAL.Entities;
using Microsoft.EntityFrameworkCore;

namespace BTK.DAL.Context
{
    public class BtkContext : DbContext
    {
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql("Host=localhost;Port=5432;Database=BTKDb;Username=postgres;Password=12345");
        }
        public DbSet<Feature> Features { get; set; }
        public DbSet< Job >Jobs { get; set; }
        public DbSet<Lesson> Lessons { get; set; }
        public DbSet <Subject> Subjects { get; set; }
        public DbSet <Team> Teams { get; set; }
        public DbSet<Mentor> Mentors { get; set; }
        public DbSet<Presentation> Presentations { get; set; }
        public DbSet<Anket> Ankets { get; set; }
        
    }
}
