using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace wpf_tester
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
        }
        List<Person> personObjs = new List<Person>();
        public MainWindow()
        {
            InitializeComponent();
            lstView.ItemsSource = personObjs;
        }
        private void BtnFill_Click(object sender, RoutedEventArgs e)

        {
            Person p = new Person() { Name = "tester", Age = 55 };
            personObjs.Add(p);
            lstView.Items.Refresh();
        }

        private void BtnCool_Click(object sender, RoutedEventArgs e)

        {

            TextBlock tb = new TextBlock { Text = "Cool!" };
            //uniGrid.Items.Add(tb);

        }

        private void Grid_Scroll(object sender, System.Windows.Controls.Primitives.ScrollEventArgs e)
        {

        }
    }
}