using System.Diagnostics;

var builder = WebApplication.CreateBuilder(args);

// CORS yapýlandýrmasý ekle
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

builder.Services.AddControllersWithViews();

var app = builder.Build();

var startInfo = new ProcessStartInfo
{
    FileName = "python3",
    Arguments = "app.py",
    WorkingDirectory = "C:\\Users\\talha\\Desktop\\AnketApi\\Anket"
};

var fastApiProcess = Process.Start(startInfo);
app.Lifetime.ApplicationStopping.Register(() => fastApiProcess.Kill());

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

// CORS'u kullanmak için ekle
app.UseCors("AllowAll");

app.UseAuthorization();


app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
