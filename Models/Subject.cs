// Models/Subject.cs
namespace BTK.Models
{
    public class Subject
    {
        public int Id { get; set; }
        public string SubjectName { get; set; }
        public string LessonName { get; set; }
        public string Image { get; set; }
        public LessonType LessonType { get; set; }
    }

    public enum LessonType
    {
        Matematik = 1,
        Turkce = 2,
        Fen = 3,
        Sosyal = 4
    }
}