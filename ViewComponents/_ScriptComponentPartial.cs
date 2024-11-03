using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _ScriptComponentPartial:ViewComponent
    {
        public IViewComponentResult Invoke() {
            return View(); 
        }
    }
}
