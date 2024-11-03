namespace BTK.DAL.Entities
{
    public class Lesson
    {
        public int LessonId { get; set; }
        public string Icon { get; set; }

        public string LessonName { get; set; }
        public string LessonDescription { get; set; }
        public string SubjectFilterLink { get; set; } 
    }
}
